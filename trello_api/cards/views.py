# views.py
from rest_framework import generics
from .models import Cards
from .serializers import CardSerializer
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.response import Response
from rest_framework import status
from columns.models import Column


class AddCardAPIView(generics.CreateAPIView):
    queryset = Cards.objects.all()
    serializer_class = CardSerializer
    permission_classes = [AllowAny]  

    def post(self, request, *args, **kwargs):
        serializer = CardSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
        column_id = request.data.get('column')
        
        try:
            column = Column.objects.get(id=column_id)
        except Column.DoesNotExist:
            return Response({'error': 'Invalid column ID'}, status=status.HTTP_400_BAD_REQUEST)
        
        last_card_position = Cards.objects.filter(column=column).order_by('-position').values_list('position', flat=True).last()
        position = last_card_position + 1 if last_card_position is not None else 0
        
        serializer.save(column=column, position=position)
        
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class EditCardAPIView(generics.RetrieveUpdateAPIView):
    queryset = Cards.objects.all()
    serializer_class = CardSerializer

    def put(self, request, *args, **kwargs):
        try:
            card_id = kwargs.get('pk')
            card = Cards.objects.get(pk=card_id)
        except Cards.DoesNotExist:
            return Response({'error': 'Card does not exist'}, status=404)
        
        request.data.pop('position', None)
        
        return self.update(request, *args, **kwargs)
    
class ReorderCardAPIView(generics.UpdateAPIView):
    queryset = Cards.objects.all()
    serializer_class = CardSerializer

    def put(self, request, *args, **kwargs):
        try:
            card_id = kwargs.get('pk')
            card = Cards.objects.get(pk=card_id)
        except Cards.DoesNotExist:
            return Response({'error': 'Card does not exist'}, status=404)
        
        new_position = request.data.get('position')
        column_id = request.data.get('column')
        
        try:
            column = Column.objects.get(id=column_id)
        except Column.DoesNotExist:
            return Response({'error': 'Invalid column ID'}, status=status.HTTP_400_BAD_REQUEST)
        
        if card.column != column:
            return Response({'error': 'Cannot move card to another column'}, status=status.HTTP_400_BAD_REQUEST)
        
        if new_position < 0:
            return Response({'error': 'Invalid position'}, status=status.HTTP_400_BAD_REQUEST)
        
        cards = Cards.objects.filter(column=column).order_by('position')
        for i, c in enumerate(cards):
            if c.id == card.id:
                continue
            if i == new_position:
                if card.position < new_position:
                    card.position = i
                else:
                    card.position = i - 1
                card.save()
                break
        
        return Response({'message': 'Card reordered successfully'}, status=status.HTTP_200_OK)