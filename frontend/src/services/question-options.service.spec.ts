import { TestBed } from '@angular/core/testing';

import { QuestionOptionsService } from './question-options.service';

describe('QuestionOptionsService', () => {
  let service: QuestionOptionsService;

  beforeEach(() => {
    TestBed.configureTestingModule({});
    service = TestBed.inject(QuestionOptionsService);
  });

  it('should be created', () => {
    expect(service).toBeTruthy();
  });
});
