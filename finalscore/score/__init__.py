from django.apps import AppConfig

class ScoreConfig(AppConfig):
    name = "score"
    def ready(self) -> None:
        import score.mysignal