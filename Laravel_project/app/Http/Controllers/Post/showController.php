<?php

namespace App\Http\Controllers\Post;

use App\Http\Controllers\Controller;
use App\Models\Category;
use App\Models\Post;
use App\Models\Tag;
use Illuminate\Http\Request;

class showController extends BaseController
{
    // Однометодные контролеры:

    public function __invoke(Post $post)
    {
        return view('post.show', compact('post'));
    }
}
