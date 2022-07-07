from abc import ABC, ABCMeta, abstractmethod
import pickle
import json


class SerializationInterface(ABC):
    @abstractmethod
    def serialize(self, data):
        pass

    @abstractmethod
    def deserialize(self, data):
        pass


class DictSerializeBin(SerializationInterface):
    def serialize(self, data):
        return pickle.dumps(data)

    def deserialize(self, sdata):
        return pickle.loads(sdata)


class DictSerialize(SerializationInterface):
    def serialize(self, data):
        return json.dumps(data)

    def deserialize(self, sdata):
        return json.loads(sdata)


class ListSerializeBin(SerializationInterface):
    def serialize(self, data):
        return pickle.dumps(data)

    def deserialize(self, sdata):
        return pickle.loads(sdata)


class ListSerialize(SerializationInterface):
    def serialize(self, data):
        return json.dumps(data)

    def deserialize(self, sdata):
        return json.loads(sdata)


class SetSerializeBin(SerializationInterface):
    def serialize(self, data):
        return pickle.dumps(data)

    def deserialize(self, sdata):
        return pickle.loads(sdata)


class SetSerialize(SerializationInterface):

    def serialize(self, data):
        return json.dumps(list(data))

    def deserialize(self, sdata):
        return set(json.loads(sdata))


class TupleSerializeBin(SerializationInterface):
    def serialize(self, data):
        return pickle.dumps(data)

    def deserialize(self, sdata):
        return pickle.loads(sdata)


class TupleSerialize(SerializationInterface):

    def serialize(self, data):
        return json.dumps(list(data))

    def deserialize(self, sdata):
        return tuple(json.loads(sdata))


if __name__ == '__main__':
    data_dict = {'one': 1, 'two': 2, 'three': 3}
    data_list = [911, 'd', 'word']
    data_tuple = (1, 2, 3)
    data_set = {1, 'ave', 'cesar'}

    print(100 * "_")
    print("Dict to Json")
    packed = DictSerialize().serialize(data_dict)
    print(f'Serialize data - {packed}')
    unpacked = DictSerialize().deserialize(packed)
    print(f'Deserialize data - {unpacked}')
    try:
        assert data_dict == unpacked, 'Not correct deserialize json dict'
        print(f'SUCCESS: JSON for Dict: {unpacked}')
    except AssertionError as error:
        print(f'{error}')
    print(100 * "_")
    print("List to Json")
    packed = ListSerialize().serialize(data_list)
    print(f'Serialize data - {packed}')
    unpacked = ListSerialize().deserialize(packed)
    print(f'Deserialize data - {unpacked}')
    try:
        assert data_list == unpacked, 'Not correct deserialize json list'
        print(f'SUCCESS: JSON for List: {unpacked}')
    except AssertionError as error:
        print(f'\n{error}\n')
    print(100 * "_")
    print("Tuple to Json")
    packed = TupleSerialize().serialize(data_tuple)
    print(f'Serialize data - {packed}')
    unpacked = TupleSerialize().deserialize(packed)
    print(f'Deserialize data - {unpacked}')
    try:
        assert data_tuple == unpacked, 'Not correct deserialize json tuple'
        print(f'SUCCESS: JSON for Tuple: {unpacked}')
    except AssertionError as error:
        print(f'\n{error}\n')

    print(100 * "_")
    print("Set to Json")
    packed = SetSerialize().serialize(data_set)
    print(f'Serialize data - {packed}')
    unpacked = SetSerialize().deserialize(packed)
    print(f'Deserialize data - {unpacked}')
    try:
        assert data_set == unpacked, 'Not correct deserialize json set'
        print(f'SUCCESS: JSON for Set: {unpacked}')
    except AssertionError as error:
        print(f'\n{error}\n')

    print(100 * "_")
    print("List to bin ")
    packed = ListSerializeBin().serialize(data_list)
    print(f'Serialize data - {packed}')
    unpacked = ListSerializeBin().deserialize(packed)
    print(f'Deserialize data - {unpacked}')
    try:
        assert data_list == unpacked, 'Not correct deserialize bin list'
        print(f'SUCCESS: BIN for List: {unpacked}')
    except AssertionError as error:
        print(f'\n{error}\n')

    print(100 * "_")
    print("Dict to bin")
    packed = DictSerializeBin().serialize(data_dict)
    print(f'Serialize data - {packed}')
    unpacked = DictSerializeBin().deserialize(packed)
    print(f'Deserialize data - {unpacked}')
    try:
        assert data_dict == unpacked, 'Not correct deserialize json dict'
        print(f'SUCCESS: BIN for Dict: {unpacked}')
    except AssertionError as error:
        print(f'\n{error}\n')

    print(100 * "_")
    print("Tuple to bin")
    packed = TupleSerializeBin().serialize(data_tuple)
    print(f'Serialize data - {packed}')
    unpacked = TupleSerializeBin().deserialize(packed)
    print(f'Deserialize data - {unpacked}')
    try:
        assert data_tuple == unpacked, 'Not correct deserialize json tuple'
        print(f'SUCCESS: BIN for Tuple: {unpacked}')
    except AssertionError as error:
        print(f'\n{error}\n')

    print(100 * "_")
    print("Set to bin")
    packed = SetSerializeBin().serialize(data_set)
    print(f'Serialize data - {packed}')
    unpacked = SetSerializeBin().deserialize(packed)
    print(f'Deserialize data - {unpacked}')
    try:
        assert data_set == unpacked, 'Not correct deserialize json set'
        print(f'SUCCESS: BIN for Set: {unpacked}')
    except AssertionError as error:
        print(f'\n{error}\n')