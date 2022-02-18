from django.db.models import query
from .models import Chart
from chart.api.serializers import ChartSerializer
from djangochannelsrestframework.generics import GenericAsyncAPIConsumer
from djangochannelsrestframework.observer import model_observer
from djangochannelsrestframework.decorators import action


class ChartConsumer(GenericAsyncAPIConsumer):
    queryset = Chart.objects.all()
    serializer_class = ChartSerializer

    @model_observer(Chart)
    async def chart_activity(self, message: ChartSerializer, observer=None, **kwargs):
        await self.send_json(message)

    @chart_activity.serializer
    def chart_activity(self, instance: Chart, action, **kwargs) -> ChartSerializer:
        '''This will return the chart serializer'''
        return ChartSerializer(instance).data

    @action()
    async def subscribe_to_chart_activity(self, **kwargs):
        await self.chart_activity.subscribe()
