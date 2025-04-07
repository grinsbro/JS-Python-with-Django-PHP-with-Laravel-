<?php

namespace App\Http\Controllers;

use App\Models\Hobby;
use Illuminate\Http\Request;

class MyHobbyController extends Controller
{
    public function index(){
        $hobby = Hobby::find(2);
        dump($hobby->name);
        dump($hobby->years);
        dump($hobby->sphere);
    }
}
