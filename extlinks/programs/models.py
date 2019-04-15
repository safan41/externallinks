from django.db import models


class Program(models.Model):
    class Meta:
        app_label = "programs"

    name = models.CharField(max_length=40)


class Organisation(models.Model):
    class Meta:
        app_label = "programs"

    name = models.CharField(max_length=40)

    program = models.ForeignKey(Program, blank=True, null=True,
                                on_delete=models.SET_NULL)

    # Some organisation use cases will want to limit link change tracking
    # to a particular list of users.
    limit_by_user = models.BooleanField(default=False)
    username_list = models.TextField(blank=True, null=True)
    # If a URL is placed here, we'll use it to regularly update username_list
    username_list_url = models.URLField(blank=True, null=True)


class Collection(models.Model):
    class Meta:
        app_label = "programs"

    name = models.CharField(max_length=40)

    organisation = models.ForeignKey(Organisation, null=True,
                                     on_delete=models.SET_NULL)
