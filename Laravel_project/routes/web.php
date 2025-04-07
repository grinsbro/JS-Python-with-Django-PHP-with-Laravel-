<?php

use App\Http\Controllers\Admin\Post\IndexAdmin;
use App\Http\Controllers\Auth\LoginController;
use Illuminate\Support\Facades\Auth;
use Illuminate\Support\Facades\Route;


// Однометодные контроллеры
Route::group(['namespace' => 'App\Http\Controllers\Post'], function () {
    Route::get('/posts', \App\Http\Controllers\Post\indexController::class)->name('post.index');

//    Route::get('/posts/update', [App\http\controllers\updateController::class,'update']);

//    Route::get('/posts/delete', [App\http\controllers\destroyController::class,'delete']);

    Route::post('/posts', \App\Http\Controllers\Post\storeController::class)->name('post.store');

    Route::get('/posts/create', \App\Http\Controllers\Post\createController::class)->name('post.create');

    Route::get('/posts/{post}', \App\Http\Controllers\Post\showController::class)->name('post.show');

    Route::get('/posts/{post}/edit', \App\Http\Controllers\Post\editController::class)->name('post.edit');
    Route::patch('/posts/{post}', \App\Http\Controllers\Post\updateController::class)->name('post.update');

    Route::delete('/posts/{post}', \App\Http\Controllers\Post\destroyController::class)->name('post.delete');

});

//Route::get('/posts', [App\http\controllers\PostController::class,'index'])->name('post.index');
//
//Route::get('/posts/update', [App\http\controllers\PostController::class,'update']);
//
//Route::get('/posts/delete', [App\http\controllers\PostController::class,'delete']);
//
//// CRUD (create, read, update, delete) через интерфейс
//
//// Создание записи:
//Route::post('/posts', [App\http\controllers\PostController::class,'store'])->name('post.store');
//
//Route::get('/posts/create', [App\http\controllers\PostController::class,'create'])->name('post.create');
//
//// Просмотр записи из базы:
//
//Route::get('/posts/{post}', [App\http\controllers\PostController::class,'show'])->name('post.show');
//
//// Изменение:
//
//Route::get('/posts/{post}/edit', [App\http\controllers\PostController::class,'edit'])->name('post.edit');
//Route::patch('/posts/{post}', [App\http\controllers\PostController::class,'update'])->name('post.update');
//
//// Удаление:
//
//Route::delete('/posts/{post}', [App\http\controllers\PostController::class,'destroy'])->name('post.delete');
//
////
//



// CRUD (create, read, update, delete) через переход по ссылкам
Route::get('/my_page', [App\Http\Controllers\MyPlaceController::class,'index']);



Route::get('/my_hobby', [App\Http\controllers\MyHobbyController::class,'index']);
Route::get('/my_friends', [App\http\controllers\MyfriendsController::class,'index']);


Route::get('/posts/first_or_create', [App\http\controllers\PostController::class,'firstOrCreate']);

Route::get('/posts/update_or_create', [App\http\controllers\PostController::class,'updateOrCreate']);

Route::get('/main', [App\http\controllers\MainController::class,'index'])->name('main.index');

Route::group(['namespace'=>'App\Http\Controllers\Admin', 'prefix'=>'admin'], function (){
    Route::group(['namespace'=>'Post'], function (){
        Route::get('/post', IndexAdmin::class)->name('admin.post.index');
        Route::get('/create', \App\Http\Controllers\Admin\Post\CreateAdmin::class)->name('admin.post.create');
        Route::get('/posts/{post}', \App\Http\Controllers\Admin\Post\ShowAdmin::class)->name('admin.post.show');
        Route::get('/posts/{post}/edit', \App\Http\Controllers\Admin\Post\EditAdmin::class)->name('admin.post.edit');
        Route::patch('/posts/{post}', \App\Http\Controllers\Admin\Post\UpdateAdmin::class)->name('admin.post.update');
    });
});

Route::get('/contacts', [App\http\controllers\ContactController::class,'index'])->name('contact.index');
Route::get('/about', [App\http\controllers\AboutController::class,'index'])->name('about.index');




Route::get('/my_city', function(){
    return "Moscow is my city";
});
Route::get('my_girl', function(){
    return 'This is my girl';
});

Auth::routes();

Route::get('/home', [App\Http\Controllers\HomeController::class, 'index'])->name('home');
