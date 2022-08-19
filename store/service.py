from store.models import Store


class StoreService:
    
    @classmethod
    def get_all_store(cls, request):
        name = request.GET.get("name")
        queryset = Store.objects.filter(owner=request.user)
        if name:
            queryset = queryset.filter(description__search=name)
        return queryset
    
    
    @classmethod
    def get_store(cls, **kwargs):
        return Store.objects.filter(**kwargs).first()
    
    
    @classmethod
    def create_store(cls, request, **kwargs):
        store =Store.objects.create(
            name=kwargs.get("name"), 
            description=kwargs.get("description"),
            owner=request.user,
            location=kwargs.get("location")
            )
        return store 
    
    
       