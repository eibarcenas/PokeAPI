from collections import Counter
from statistics import mean, median, variance
from typing import Any, Dict, List

import httpx
from fastapi import status

from app.api.schemas.berries import BerriesStats
from app.core.exceptions.berries import BerriesNamesNotFound, BerryNotFound
from app.settings import settings


class BerriesService:
    def __init__(self) -> None:
        self.poke_api = settings.app_poke_api

    async def _get_all_berries_names(self) -> List[str]:
        async with httpx.AsyncClient() as client:
            response = await client.get(f"{self.poke_api}/berry")
            if response.status_code == status.HTTP_200_OK:
                data = response.json()
                berries = [berry["name"] for berry in data["results"]]
                return berries
            else:
                raise BerriesNamesNotFound(response.status_code, response.text)

    async def _get_growth_time(self, berry_name: str) -> List[int]:
        async with httpx.AsyncClient() as client:
            response = await client.get(f"{self.poke_api}/berry/{berry_name}")
            if response.status_code == status.HTTP_200_OK:
                data = response.json()
                return data["growth_time"]
            else:
                raise BerryNotFound(
                    response.status_code,
                    f"Failed to fetch growth time for {berry_name}",
                )

    async def _get_growth_times(self, berries_names: List[str]) -> List[int]:
        growth_times = []
        for berry_name in berries_names:
            growth_time = await self._get_growth_time(berry_name)
            growth_times.append(growth_time)
        return growth_times

    def _calculate_stats(self, growth_times: List[int]) -> Dict[str, Any]:
        return {
            "min_growth_time": min(growth_times),
            "median_growth_time": median(growth_times),
            "max_growth_time": max(growth_times),
            "variance_growth_time": variance(growth_times),
            "mean_growth_time": mean(growth_times),
            "frequency_growth_time": dict(Counter(growth_times)),
        }

    async def get_stats(self) -> BerriesStats:
        berries_names = await self._get_all_berries_names()
        growth_times = await self._get_growth_times(berries_names)
        stats = self._calculate_stats(growth_times)
        # response
        stats["berries_names"] = berries_names
        return BerriesStats(**stats)
