from store.models import Store


class StoreService:
    
    @classmethod
    def get_all_store(cls, request):
        return Store.objects.filter(owner=request.user)
    
    
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
    
    
       