import graphene

from .types import CarType
from .models import Car


class CarsResolver(graphene.ObjectType):
    cars = graphene.List(CarType)
    car = graphene.Field(CarType, id=graphene.Int(),)

    def resolve_cars(_, info):
        return Car.objects.filter(is_published=True)

    def resolve_car(_, info, **kwargs):
        id = kwargs.get('id')
        if id is not None:
            return Car.objects.get(id=id)


class PublishCarMutation(graphene.Mutation):
    class Arguments:
        id = graphene.Int()

    msg = graphene.String()

    def mutate(self, info, id):
        car = Car.objects.get(id=id)
        car.is_published = True
        car.save()
        return PublishCarMutation(msg = "the car was been published")


class HideCarMutaiton(graphene.Mutation):
    class Arguments:
        id = graphene.Int()

    msg = graphene.String()

    def mutate(self, info, id):
        car = Car.objects.get(id=id)
        car.is_published = False
        car.save()
        return HideCarMutaiton(msg="the car was been hide from list")



class CreateCarMutation(graphene.Mutation):
    class Arguments:
        name = graphene.String()
        reg_number = graphene.String()

    car = graphene.Field(CarType)
    msg = graphene.String()

    def mutate(self, info, **kwargs):
        name = kwargs.get('name')
        reg_number = kwargs.get('reg_number')
        if name and reg_number:
            try:
                car = Car.objects.create(name=name, reg_number=reg_number)
                return CreateCarMutation(car=car, msg="the car successfuly added!")
            except:
                return CreateCarMutation(msg="the car already exist!")


class UpdateCarMutation(graphene.Mutation):
    class Arguments:
        id = graphene.Int()
        name = graphene.String()
        reg_number = graphene.String()

    car = graphene.Field(CarType)

    def mutate(self, info, **kwargs):	# self, info, {id, name, reg_number}
        id = kwargs.get('id')
        name = kwargs.get('name')
        reg_number = kwargs.get('reg_number')
        if id is not None:
            car = Car.objects.get(id=id)
            if name:
                car.name = name
            if reg_number:
                car.reg_number = reg_number
            car.save()
            return UpdateCarMutation(car=car)


class DeleteCarMutation(graphene.Mutation):
    class Arguments:
        id = graphene.Int()
        name = graphene.String()
        reg_number = graphene.String()

    car = graphene.Field(CarType)

    def mutate(self, info, **kwargs):
        id = kwargs.get('id')
        name = kwargs.get('name')
        reg_number = kwargs.get('reg_number')
        if id is not None:
            Car.objects.get(id=id).delete()
        elif name is not None:
            Car.objects.get(name=name).delete()
        elif reg_number is not None:
            Car.objects.get(reg_number=reg_number).delete()
