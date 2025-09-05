from dataclasses import dataclass
from heapq import heappush, heappop, nlargest
from collections import defaultdict
from typing import Counter


@dataclass(frozen=True)
class UserFilmView:
    user_id: str
    film_id: str


def get_top_3_films_per_user(events: list[UserFilmView]) -> dict[str, list]:
    """Calculates the top three films per user from a list of input events.

    :param events: UserFilmView objects representing a film viewed by a user.
    :return: Dictionary with the user_id as key and a list of most watched films in descending order as value. There are up to 3 film ids in the list.
    """
    # Count views per film and user
    # {(user_id, film_id}: num_view}
    # {(1, 10): 5, (1, 20): 2, (1, 30): 1}
    film_views_per_user = Counter(events)
    print(film_views_per_user)

    # Find top 3 most viewed movies per user
    # {user_1: [(10, 5), (20, 2), (30, 1)]}
    users_top_3_film_views = defaultdict(list)

    for user_film_view, count in film_views_per_user.items():
        heappush(users_top_3_film_views[user_film_view.user_id], (count, user_film_view.film_id))
        if len(users_top_3_film_views[user_film_view.user_id]) > 3:
            heappop(users_top_3_film_views[user_film_view.user_id])

    print(users_top_3_film_views)

    return {
        user: [film for count, film in nlargest(3, heap)]
        for user, heap in users_top_3_film_views.items()
    }

if __name__ == '__main__':
    input_data = [
        (1, 10),
        (1, 20),
        (1, 10),
        (1, 30),
        (1, 10),
        (2, 20),
        (2, 20),
        (2, 30),
        (2, 40),
        (3, 30),
        (3, 30),
        (3, 30),
        (3, 40),
        (3, 40),
        (3, 50),
        (4, 30),
        (4, 30),
        (4, 30),
    ]
    input_data = [UserFilmView(e[0], e[1]) for e in input_data]

    print(get_top_3_films_per_user(input_data))
