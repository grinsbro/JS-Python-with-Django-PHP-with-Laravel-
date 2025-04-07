@extends('layouts.main')
@section('content')
    <div>
        <div>
            <a href="{{route('post.create')}}" class="btn btn-primary mb-3">Создать пост</a>
        </div>
        @foreach($posts as $post)
        <div><a href="{{ route('post.show', $post->id) }}">{{$post->id}}. {{$post->title}}</a></div>
        @endforeach

{{--        Продолжение пагинации--}}

        <div class="mt-3">
            {{$posts->withQueryString()->links('pagination::bootstrap-4')}}
        </div>
    </div>
@endsection
