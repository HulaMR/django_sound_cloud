from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.response import Response

from .. import serializer
<<<<<<< HEAD
from ..services import google, spotify
=======
from ..services.google import check_google_auth
>>>>>>> origin/master


def google_login(request):
    return render(request, 'oauth/google_login.html')


<<<<<<< HEAD
def spotify_login(request):
    return render(request, 'oauth/spotify_login.html')


=======
>>>>>>> origin/master
@api_view(["POST"])
def google_auth(request):
    google_data = serializer.GoogleAuth(data=request.data)
    if google_data.is_valid():
<<<<<<< HEAD
        token = google.check_google_auth(google_data.data)
        return Response(token)
    else:
        return AuthenticationFailed(code=403, detail='Bad data Google')


@api_view(['GET'])
def spotify_auth(request):
    token = spotify.spotify_auth(request.query_params.get('code'))
    return Response(token)
=======
        token = check_google_auth(google_data.data)
        return Response(token)
    else:
        return AuthenticationFailed(code=403, detail='Bad data Google')
>>>>>>> origin/master
