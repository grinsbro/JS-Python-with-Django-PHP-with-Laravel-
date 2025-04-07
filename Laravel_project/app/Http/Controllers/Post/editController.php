<?php

namespace App\Http\Controllers\Post;

use App\Http\Controllers\Controller;
use App\Models\Category;
use App\Models\Post;
use App\Models\Tag;
use Illuminate\Http\Request;

class editController extends BaseController
{
    // Однометодные контролеры:

    public function __invoke()
    {
        $categories = Category::all();
        $tags = Tag::all();
        return view('post.edit', compact('categories', 'post', 'tags'));
    }
}
