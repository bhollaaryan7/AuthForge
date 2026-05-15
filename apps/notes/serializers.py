from rest_framework import serializers

from .models import Note, Tag


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ["id", "name"]


class NoteSerializer(serializers.ModelSerializer):
    tags = serializers.ListField(
        child=serializers.CharField(),
        write_only=True,
        required=False
    )

    tag_objects = TagSerializer(
        source="tags",
        many=True,
        read_only=True
    )

    class Meta:
        model = Note
        fields = [
            "id",
            "title",
            "content",
            "tags",
            "tag_objects",
            "created_at",
            "updated_at",
        ]

        read_only_fields = [
            "id",
            "created_at",
            "updated_at",
        ]

    def create(self, validated_data):
        tags_data = validated_data.pop("tags", [])

        note = Note.objects.create(**validated_data)

        for tag_name in tags_data:
            tag, _ = Tag.objects.get_or_create(name=tag_name)
            note.tags.add(tag)

        return note
