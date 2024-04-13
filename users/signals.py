from django.db.models.signals import post_save
from users.models import CustomUser,UserProfile, Groups
from django.dispatch import receiver
from django.contrib.auth.models import Group


@receiver(post_save, sender=CustomUser)
def Createprofile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user = instance)
        
@receiver(post_save, sender=Groups)
def update_permission(sender, instance, created, **kwargs):
    if created:
        owner_group, _ = Group.objects.get_or_create(name='Owner')
        
        instance.Owner.groups.add(owner_group)
        
        staff_group,_ = Group.objects.get_or_create(name='staff')
        
        for member in instance.members.exclude(id=instance.Owner.id):
            member.groups.add(staff_group)