package com.example.foodshare.models;

import com.google.firebase.database.Exclude;
import com.google.firebase.database.IgnoreExtraProperties;

import java.util.HashMap;
import java.util.Map;

@IgnoreExtraProperties
public class Offer {
    public String uid;
    public String author;
    public String name;
    public String comments;
    public String address;
    public String picture;
    public String postid;
    public String status;


    public Offer() {
        // Default constructor required for calls to DataSnapshot.getValue(Post.class)
    }

    public Offer(String uid, String author, String name, String comments, String address, String picture, String postid, String status) {
        this.uid = uid;
        this.author = author;
        this.name = name;
        this.address = address;
        this.comments = comments;
        this.picture = picture;
        this.postid = postid;
        this.status = status;
    }

    // post_to_map
    @Exclude
    public Map<String, Object> toMap() {
        HashMap<String, Object> result = new HashMap<>();
        result.put("uid", uid);
        result.put("author", author);
        result.put("name", name);
        result.put("comments", comments);
        result.put("picture", picture);
        result.put("address", address);
        result.put("postid", postid);
        result.put("status", status);


        return result;
    }

}
