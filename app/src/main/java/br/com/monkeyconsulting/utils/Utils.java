package br.com.monkeyconsulting.utils;

import java.util.Optional;

public class Utils {

    public static <T> Object validaRetorno(Optional<T> optional) {
        if (optional.isPresent())
            return optional.orElseThrow(() -> new RuntimeException("Houve um problema ao obter o Objeto"));
        return null;
    }
}
