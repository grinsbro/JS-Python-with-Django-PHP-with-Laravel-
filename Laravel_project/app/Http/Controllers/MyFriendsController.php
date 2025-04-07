<?php

namespace App\Http\Controllers;

use App\Models\Friend;
use Illuminate\Http\Request;

class MyFriendsController extends Controller
{
    public function index(){
        $friend = Friend::find(1);
        dump($friend->name);
        dump($friend->age);
        dump($friend->gender);
        dump($friend->country);

    }
}
