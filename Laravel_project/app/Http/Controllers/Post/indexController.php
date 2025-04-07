<?php

namespace App\Http\Controllers\Post;

use App\Http\Controllers\Controller;
use App\Http\Filters\PostFilter;
use App\Http\Requests\Post\FilterRequest;
use App\Models\Category;
use App\Models\Post;
use App\Models\Tag;
use Illuminate\Http\Request;

class indexController extends BaseController
{
    // Однометодные контролеры:

    public function __invoke(FilterRequest $request)
    {

        $data = $request->validated();

        // $query = Post::query(); // Создается динамичный запрос(несколько фильтров)

        $filter = app()->make(PostFilter::class, ['queryParams' => array_filter($data)] );

        $posts = Post::filter($filter)->paginate(10);


        // Пагинация:
//        $posts = Post::paginate(10); // Пагинация нужна, чтобы снизить нагрузку на сайт. Продолжение есть в шаблоне blade.php
           return view('post.index', compact('posts'));
    }
}
