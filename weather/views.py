from base.mixin import admin_mixin
from weather import mixins


class WeatherTypeListCreateView(mixins.BaseWeatherTypViewMixin,
                                admin_mixin.ListCreateAPIView):
    """
    <div style='text-align: justify;'>
    This api is to be used to create weather type like normal, hot, cold
    or to see all weather types. Only Authenticated admin super will be able to see it.
    when an admin user try to send this request:
    <ul>
        <li> It performs create operation after sending a post request </li>
        <li> It gives a list of weather after sending a get request.</li>
    </ul>
    </div>
    """
    pass


class WeatherTypeUpdateDeleteDestroyView(mixins.BaseWeatherTypViewMixin,
                                         admin_mixin.RetrieveUpdateDestroyAPIView):
    """
    <div style='text-align: justify;'>
    This API is used to get four HTTP methods functionality
    like get, put, patch, and delete for weather type crud operation.
    it is only for Authenticated admin users. <br/>Non-Authenticated users
    or simple users can't access it. when an admin user try to send this request:
    <ul>
        <li> It performs an update operation after sending a put request.</li>
        <li> It performs a partial update operation after sending a patch request.</li>
        <li> It performs a delete operation after sending a delete request.</li>
        <li> It gives the weather details after sending a get request.</li>
    </ul>
    <br/>
    Also, an admin able to set the temperature range(high, low) for each weather type using patch request.
    <pre>
    {
      "temp_min": 45,
      "temp_max": 345
    }
    </pre>
    </div>
    """
    pass
