import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { ApiPaths } from 'src/data/api-paths';
import { Env } from 'src/data/env';
import { Questionnaire } from 'src/models/questionnaire';

@Injectable({
  providedIn: 'root'
})
export class QuestionnariesService {
  constructor(private httpClient: HttpClient) { }

  getQuestionnaries() {
    return this.httpClient.get<JSON>(`${Env.ApiUrl}/${ApiPaths.Questionnaries}/`);
  }

  getQuestionnarie(id: number) {
    return this.httpClient.get<JSON>(`${Env.ApiUrl}/${ApiPaths.Questionnaries}/${id}/`);
  }

  updateQuestionnarie(questionnarie: Questionnaire) {
    return this.httpClient.put<JSON>(
      `${Env.ApiUrl}/${ApiPaths.Questionnaries}/${questionnarie.id}/`,
      questionnarie
    );
  }
}
