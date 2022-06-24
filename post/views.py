from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import permissions, status

from post.serializers import JobPostSerializer
from .models import (
    JobPostSkillSet,
    JobType,
    JobPost,
    Company
)
from django.db.models.query_utils import Q


class SkillView(APIView):

    permission_classes = [permissions.AllowAny]

    def get(self, request):
        skills = self.request.query_params.getlist('skills', '')
        print("skills = ", end=""), print(skills)

        return Response(status=status.HTTP_200_OK)


class JobView(APIView):

    def post(self, request):
        job_type = request.data.get("job_type", None)
        job_type_instance = JobType.objects.get(id=job_type)
        company_name = request.data.get("company_name", None)
        company_instance = Company.objects.get(company_name=company_name)
        print(company_instance)
        job_serializer = JobPostSerializer(data=request.data)
        if job_serializer.is_valid():
            job_serializer.save(job_type=job_type_instance, company=company_instance)
            return Response(job_serializer.data, status=status.HTTP_200_OK)
        return Response({'message': '존재하지 않는 job_type입니다'},status=status.HTTP_400_BAD_REQUEST)
    

