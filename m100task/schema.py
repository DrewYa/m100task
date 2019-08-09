import graphene

from cars.resolver import CarsResolver
from cars.resolver import HideCarMutaiton, PublishCarMutation
from cars.resolver import UpdateCarMutation, CreateCarMutation, DeleteCarMutation


class Query(
    CarsResolver
):
    """Parent query class inherited from all real query classes
    """
    pass


class Mutation(graphene.ObjectType):
    """Parent Mutation class containing all mutations
    """
    publish_car = PublishCarMutation.Field()
    hide_car = HideCarMutaiton.Field()

    create_car = CreateCarMutation.Field()
    update_car = UpdateCarMutation.Field()
    delete_car = DeleteCarMutation.Field()


schema = graphene.Schema(
    query=Query,
    mutation=Mutation,
)

# schema.execute(
# '''
#   query {
#     cars {
#       id
#       name
#       reg_number
#     }
#   }
# '''
# )
