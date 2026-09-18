from heapq import heappop, heappush
from typing import Optional

Graph = dict[str, list[tuple[str, float]]]


def uniform_cost_search(
    graph: Graph,
    start: str,
    goal: str,
) -> Optional[tuple[list[str], float]]:
    """Mencari jalur dengan biaya/waktu terendah dari start ke goal menggunakan UCS."""


    # Validasi awal: jika simpul start tidak ada di dalam graf
    if start not in graph:
        return None

    frontier: list[tuple[float, int, str]] = []
    heappush(frontier, (0.0, 0, start))

    came_from: dict[str, Optional[str]] = {start: None}
    cost_so_far: dict[str, float] = {start: 0.0}

    counter = 1

    while frontier:
        current_cost, _, current = heappop(frontier)

        # Abaikan entri yang sudah usang dalam antrean prioritas
        if current_cost > cost_so_far.get(current, float("inf")):
            continue

        # Tujuan tercapai (Goal Test)
        if current == goal:
            path = _reconstruct_path(came_from, goal)
            return path, current_cost

        for next_state, step_cost in graph.get(current, []):
            if step_cost < 0:
                raise ValueError(
                    "UCS mensyaratkan bobot biaya bernilai non-negatif."
                )

            new_cost = current_cost + step_cost

            if (
                next_state not in cost_so_far
                or new_cost < cost_so_far[next_state]
            ):
                cost_so_far[next_state] = new_cost
                came_from[next_state] = current

                heappush(
                    frontier,
                    (new_cost, counter, next_state),
                )
                counter += 1

    return None

def _reconstruct_path(
    came_from: dict[str, Optional[str]],
    goal: str,
) -> list[str]:
    """Merekonstruksi urutan jalur dari start menuju goal."""
    path: list[str] = []
    current: Optional[str] = goal

    while current is not None:
        path.append(current)
        current = came_from.get(current)

    path.reverse()
    return path