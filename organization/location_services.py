from .models import State, City, Location
import datetime
__author__ = 'ravi'


class LocationORM(object):
    @staticmethod
    def add_state(state_name):
        state = State()
        state.state_name = state_name
        state.lastupd_dttm = datetime.datetime.now()
        try:
            state.save()
        except Exception as ex:
            raise ex

    @staticmethod
    def is_state_exists(state_name):
        state = False
        try:
            state = State.objects.get(state_name=state_name)
            if state:
                state = True
        except Exception as ex:
            raise ex
        return state

    @staticmethod
    def get_all_state():
        state = None
        try:
            state = State.objects.all().order_by('state_name')
        except Exception as ex:
            raise ex
        return state

    @staticmethod
    def add_city(city_name, state_name):
        city = City()
        city.city_name = city_name
        city.state_name = state_name
        city.lastupd_dttm = datetime.datetime.now()
        try:
            city.save()
        except Exception as ex:
            raise ex

    @staticmethod
    def get_all_city():
        city = None
        try:
            city = City.objects.all().order_by('city_name')
        except Exception as ex:
            raise ex
        return city

    @staticmethod
    def add_location(state_name, city_name, sub_city, pin_code):
        location = Location()
        location.state_name = state_name
        location.city_name = city_name
        location.sub_city = sub_city
        location.pin_code = pin_code
        location.status = '1'
        location.lastupd_dttm = datetime.datetime.now()
        try:
            location.save()
        except Exception as ex:
            raise ex

    @staticmethod
    def get_all_location():
        location = None
        try:
            location = Location.objects.all()
        except Exception as ex:
            raise ex
        return location
