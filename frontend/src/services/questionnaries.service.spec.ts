import { TestBed } from '@angular/core/testing';

import { QuestionnariesService } from './questionnaries.service';

describe('QuestionnariesService', () => {
  let service: QuestionnariesService;

  beforeEach(() => {
    TestBed.configureTestingModule({});
    service = TestBed.inject(QuestionnariesService);
  });

  it('should be created', () => {
    expect(service).toBeTruthy();
  });
});
