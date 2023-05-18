import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { ApiPaths } from 'src/data/api-paths';
import { Env } from 'src/data/env';

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

  saveQuestionnarie(questionnarie: any) {
    return this.httpClient.put<JSON>(`${Env.ApiUrl}/${ApiPaths.Questionnaries}/${questionnarie.id}/`, questionnarie);
  }
}
