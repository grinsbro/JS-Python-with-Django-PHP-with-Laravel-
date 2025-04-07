<?php

namespace App\Http\Controllers;

use App\Models\Category;
use App\Models\Post;
use App\Models\Tag;
use Illuminate\Http\Request;

class PostController extends Controller
{
    public function index()
    {
//        $post = Post::where('likes','>=',20)->first();
//
//        dump($post->title);
//
//        dd('end'); // Таким образом можно находить данные в таблице


//        $category = Category::find(1);

        $post = Post::find(1);
        $category = Category::find(1);
        $tag = Tag::find(1);
        dd($post->tags);

        return view('post.index', compact('posts'));

    }


    // Так создаются записи в таблицу
//    public function create()
//    {
//        $postsArr = [
//          [
//              'title' => 'title from phpStorm',
//              'content' => 'some content',
//              'image' => 'image.jpg',
//              'likes' => 20,
//              'is_published' => 1,
//          ],
//          [
//              'title' => 'another title from phpStorm',
//              'content' => 'some another content',
//              'image' => 'image.jpg',
//              'likes' => 30,
//              'is_published' => 1,
//          ],
//        ];
//
//        foreach ($postsArr as $item) {
//            Post::create($item);
//        }
//
//        dd('created');
//    }

//Обновляю данные в таблице:
//    public function update(){
//        $post = Post::find(6);
//        $post->update([
//            'title' => 'updated',
//            'content' => 'updated',
//            'image' => 'updated',
//            'likes' => 2000,
//            'is_published' => 1,
//        ]);
//        dd('updated');
//    }

//Удаляю данные в таблице:

//    public function delete() {
//        $post = Post::find(2);
//        $post->delete();
//        dd('deleted');
//    }
    // Можно также прописать "мягкое удаление" (когда запись вроде удаляется, но ее можно восстановить).
    // В файле с миграцией нужно прописать $table->softDeletes()
    // Также в файле модели нужно прописать использование трейта SoftDeletes (use SoftDeletes)

    // Восстановить запись можно так:
//    public function delete(){
//        $post = Post::withTrashed()->find(2);
//        $post->restore();
//        dd('deleted');
//    }

    // firstOrCreate - это метод для поиска записи в базе, но если ее нет, то он создает такую запись
    // updateOrCreate - такой же метод, но он обновляет значения

//    public function firstOrCreate() {
//
//        $anotherPost = [
//            'title' => 'some post',
//            'content' => 'some content',
//            'image' => 'someimage.jpg',
//            'likes' => 200214,
//            'is_published' => 1,
//        ];
//
//        $post = Post::firstOrCreate([
//            'title' => 'some post'
//        ],[
//            'title' => 'some post',
//            'content' => 'some content',
//            'image' => 'someimage.jpg',
//            'likes' => 200214,
//            'is_published' => 1
//        ]);
//
//        dump($post->content);
//        dd('finished');
//    }

//    public function updateOrCreate() {
//        $somePost = [
//            'title' => 'Another post title',
//            'content' => 'Another post content',
//            'image' => 'another_post_image.jpg',
//            'likes' => 10231,
//            'is_published' => 1,
//        ];
//        $post = Post::updateOrCreate([
//            'title' => 'Another post not title',
//        ], [
//            'title' => 'Another post not title',
//            'content' => 'Another post content',
//            'image' => 'another_post_image.jpg',
//            'likes' => 10231,
//            'is_published' => 1
//        ]);
//        dump($post->title);
//        dd('finished');
//    }

// Create через интерфейс

    public function create()
    {
        $categories = Category::all();
        $tags = Tag::all();

        return view('post.create', compact('categories', 'tags'));
            }

    public function store()
    {

        $data = request()->validate([
            'title' => 'required|',
            'content' => '',
            'image' => '',
            'category_id' => '',
            'tags' => 'nullable|array',
        ]);

        $post = Post::create($data);
        if (isset($data['tags'])) {
            $post->tags()->attach($data['tags']);
        }

        return redirect()->route('post.index');
    }

// Просмотр записи:
    public function show(Post $post)
    {
        // dd ($post->title);
        return view('post.show', compact('post'));
    }

// Редактирование записи:

    public function edit(Post $post)
    {
        $categories = Category::all();
        $tags = Tag::all();
        return view('post.edit', compact('categories', 'post', 'tags'));
    }

    public function update(Post $post)
    {
        $data = request()->validate([
            'title' => '',
            'content' => '',
            'image' => '',
            'category_id' => '',
            'tags' => '',
        ]);
        $tags = $data['tags'];
        unset($data['tags']);

        $post->update($data);
        $post->tags()->sync($tags);

        return redirect()->route('post.show', $post->id);
    }

// Удаление Записи:

    public function destroy(Post $post)
    {
        $post->delete();
        return redirect()->route('post.index');
    }



}
