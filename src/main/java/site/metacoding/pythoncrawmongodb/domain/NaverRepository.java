package site.metacoding.pythoncrawmongodb.domain;

import org.springframework.data.mongodb.repository.MongoRepository;

public interface NaverRepository extends MongoRepository<Naver, String> {
    
}
