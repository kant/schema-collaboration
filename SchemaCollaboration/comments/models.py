from django.db import models

from core.models import CreateModifyOn
from core.models import Person, Datapackage


class AbstractComment(CreateModifyOn):
    datapackage = models.ForeignKey(Datapackage, on_delete=models.PROTECT)
    author = models.ForeignKey(Person, on_delete=models.PROTECT)
    text = models.TextField()
    private = models.BooleanField()

    class Meta:
        abstract = True

    def __str__(self):
        if self.text is None:
            text = ''
        else:
            text = f'{self.text[:20]}...'

        return f'Author:{self.author}-{text}'


class Comment(AbstractComment):
    pass

# TODO (a comment that would be displayed with a checkbox to be done) were never implemented
# The model was written: for now I'll leave it here in case that I get to do it at some point
# class ToDo(AbstractComment):
#     done = models.BooleanField()
#     done_by = models.ForeignKey(Person, related_name='done_by_author', null=True, blank=True,
#                                 on_delete=models.PROTECT)
#     done_on = models.DateField(null=True, blank=True)
#
#     class Meta:
#         verbose_name_plural = 'TO DOs'
