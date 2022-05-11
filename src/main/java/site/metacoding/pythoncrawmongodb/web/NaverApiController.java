package site.metacoding.pythoncrawmongodb.web;

import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RestController;

import lombok.RequiredArgsConstructor;
import site.metacoding.pythoncrawmongodb.domain.NaverRepository;

@RequiredArgsConstructor
@RestController
public class NaverApiController {
    
    private final NaverRepository naverRepository;

    @GetMapping("/navers")
    public ResponseEntity<?> findAll() {
        return new ResponseEntity<>(naverRepository.findAll(), HttpStatus.OK);
    }
}
