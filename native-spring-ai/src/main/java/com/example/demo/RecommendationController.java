package com.example.demo;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestParam;

@Controller
public class RecommendationController {

    @Autowired
    private RecommendationLearning recommendationLearning;

    @GetMapping("/")
    public String form(Model model) {
        return "form";
    }

    @PostMapping("/recommend")
    public String recommend(@RequestParam String role, @RequestParam String area, @RequestParam String level, Model model) {
        String recommendation = recommendationLearning.getRecommendation(role, area, level);
        System.out.println(recommendation);
        model.addAttribute("recommendation", recommendation);
        return "result";
    }

}