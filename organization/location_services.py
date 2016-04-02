from .models import State
import datetime


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
            state = State.objects.all()
        except Exception as ex:
            raise ex
        return state
