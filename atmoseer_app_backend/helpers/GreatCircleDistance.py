from math import atan2, cos, radians, sin, sqrt


class GreatCircleDistance:
    EARTH_RADIUS_KM = 6371.0

    def _degrees_to_radians(self, *degrees: float) -> list[float]:
        return [radians(degree) for degree in degrees]

    def _haversine_function(self, theta: float) -> float:
        return sin(theta / 2) ** 2

    def _haversine_formula(
        self, lat1: float, lon1: float, lat2: float, lon2: float
    ) -> float:
        delta_lat = lat2 - lat1
        delta_lon = lon2 - lon1
        return self._haversine_function(delta_lat) + cos(lat1) * cos(
            lat2
        ) * self._haversine_function(delta_lon)

    def _inverse_haversine_function(self, y: float) -> float:
        return 2 * atan2(sqrt(y), sqrt(1 - y))

    def get_distance(self, lat1: float, lon1: float, lat2: float, lon2: float) -> float:
        lat1, lon1, lat2, lon2 = self._degrees_to_radians(lat1, lon1, lat2, lon2)
        haversine_theta = self._haversine_formula(lat1, lon1, lat2, lon2)
        theta_angle = self._inverse_haversine_function(haversine_theta)
        arc_length = self.EARTH_RADIUS_KM * theta_angle
        return arc_length


great_circle_distance = GreatCircleDistance()
