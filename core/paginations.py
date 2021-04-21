from rest_framework import pagination



class PublicPagination(pagination.LimitOffsetPagination):
    default_limit = 12
