package com.example.demo;

import org.springframework.stereotype.Service;
import org.springframework.ai.chat.ChatClient;
import org.springframework.ai.chat.prompt.Prompt;
import org.springframework.ai.chat.prompt.PromptTemplate;

@Service
public class RecommendationLearning {

    private final ChatClient chatClient;

    public RecommendationLearning(ChatClient chatClient) {
        this.chatClient = chatClient;
    }

    public String getRecommendation(String role, String area, String level) {
        String message = """
                You are acting as an Oracle Cloud Infrastructure specialist recommendation service.
                Provide a course and certification suggestion to a user based on their preferences. Please don't use markdown syntax.
                They prefer %s as the role, %s as the area of interest and %s as the level.
            """.formatted(role, area, level);
        PromptTemplate promptTemplate = new PromptTemplate(message);
        Prompt prompt = promptTemplate.create();
        return chatClient.call(prompt).getResult().getOutput().getContent();
    }
}