package br.com.monkeyconsulting.handler;

import jakarta.servlet.http.HttpServletRequest;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.ControllerAdvice;
import org.springframework.web.bind.annotation.ExceptionHandler;

@ControllerAdvice
public class GlobalExceptionHandler {

    @ExceptionHandler(Exception.class)
    public String handleGlobalException(HttpServletRequest request, Exception ex, Model model) {

        if (ex instanceof RuntimeException) {
            if (ex.getMessage().contains("Telefone ja cadastrado!")) {
                System.out.println("adaddadad");
            }
            model.addAttribute("errorMessage", ex.getMessage()); // Adiciona a mensagem de erro ao Model
        }

        return "error"; // Retorna o nome do arquivo HTML de erro (sem a extensão .html)
    }
}