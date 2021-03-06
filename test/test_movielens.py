from unittest import TestCase

from tensorrec import TensorRec
from tensorrec.loss_graphs import wmrb_loss

from test.datasets import get_movielens_100k


class MovieLensTestCase(TestCase):

    @classmethod
    def setUpClass(cls):
        cls.movielens_100k = get_movielens_100k()

    def test_movie_lens_fit(self):
        """
        This test checks whether the movielens getter works and that the resulting data is viable for fitting/testing a
        TensorRec model.
        """
        train_interactions, test_interactions, user_features, item_features = self.movielens_100k

        model = TensorRec()
        model.fit(interactions=train_interactions, user_features=user_features, item_features=item_features)
        predictions = model.predict(user_features=user_features,
                                    item_features=item_features)

        self.assertIsNotNone(predictions)

    def test_movie_lens_fit_wmrb(self):
        """
        This test checks whether the movielens getter works and that the resulting data is viable for fitting/testing a
        TensorRec model.
        """
        train_interactions, test_interactions, user_features, item_features = self.movielens_100k

        model = TensorRec(loss_graph=wmrb_loss)
        model.fit(interactions=train_interactions, user_features=user_features, item_features=item_features)
        predictions = model.predict(user_features=user_features,
                                    item_features=item_features)

        self.assertIsNotNone(predictions)
