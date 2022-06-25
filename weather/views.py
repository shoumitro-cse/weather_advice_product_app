from rest_framework.permissions import IsAuthenticated
from weather.models import WeatherType
from weather.serializer import WeatherTypeSerializer
from base import mixin


class WeatherTypeListCreateView(mixin.ListCreateAPIView):
    """
    <div style='text-align: justify;'>
    This api is to be used to create weather type like normal, hot, cold
    or to see all weather types. Only Authenticated admin super will be able to see it.
    when an admin user:
    <ul>
        <li> It performs create operation after sending a post request </li>
        <li> It gives a list of weather after sending a get request.</li>
    </ul>
    </div>
    """

    serializer_class = WeatherTypeSerializer
    permission_classes = [IsAuthenticated, ]
    queryset = WeatherType.objects.all()


class WeatherTypeUpdateDeleteDestroyView(mixin.RetrieveUpdateDestroyAPIView):
    """
    <div style='text-align: justify;'>
    This API is used to get four HTTP methods functionality
    like get, put, patch, and delete for weather type crud operation.
    it is only for Authenticated admin users. <br/>Non-Authenticated users
    or simple users can't access it. when an admin user
    <ul>
        <li> It performs an update operation after sending a put request.</li>
        <li> It performs a partial update operation after sending a patch request.</li>
        <li> It performs a delete operation after sending a delete request.</li>
        <li> It gives the weather details after sending a get request.</li>
    </ul>
    </div>
    """

    serializer_class = WeatherTypeSerializer
    permission_classes = [IsAuthenticated, ]
    queryset = WeatherType.objects.all()
