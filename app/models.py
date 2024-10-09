from django.db import models
# Create your models here.
class EngagementPost(models.Model):
    tenant_id=models.IntegerField()
    post_content=models.TextField()
    created_at=models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.post_content

class EngagementPostContent(models.Model):
    post=models.ForeignKey(EngagementPost,on_delete=models.CASCADE)
    content_url=models.CharField(max_length=100)


    

class EngagementPostProduct(models.Model):
    post=models.ForeignKey(EngagementPost,on_delete=models.CASCADE)
    product_name=models.CharField(max_length=255)
    product_image=models.CharField(max_length=255)
    sku=models.CharField(max_length=255)
    def __str__(self):
        return self.product_name

class Collection(models.Model):
    collection_name=models.CharField(max_length=255)
    def __str__(self):
        return self.collection_name


class EngagementPostCollection(models.Model):
    post=models.ForeignKey(EngagementPost,on_delete=models.CASCADE)
    collection=models.ForeignKey(Collection,on_delete=models.CASCADE)
    duration_in_seconds=models.IntegerField()
    def __str__(self):
        return str(self.duration_in_seconds)
