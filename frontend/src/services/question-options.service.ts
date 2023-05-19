import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { ApiPaths } from 'src/data/api-paths';
import { Env } from 'src/data/env';
import { QuestionOption } from 'src/models/question_option';

@Injectable({
  providedIn: 'root'
})
export class QuestionOptionsService {
  constructor(private httpClient: HttpClient) { }

  public createQuestionOption(questionId: number) {
    let questionOption: QuestionOption = new QuestionOption();

    questionOption.question = questionId;
    questionOption.text = "Texto da nova opção";

    return this.httpClient.post<JSON>(`${Env.ApiUrl}/${ApiPaths.QuestionOptions}/`, questionOption);
  }

  public getQuestionOption(id: number) {
    return this.httpClient.get<JSON>(`${Env.ApiUrl}/${ApiPaths.QuestionOptions}/${id}/`);
  }

  public updateQuestionOption(questionOption: QuestionOption) {
    return this.httpClient.put<JSON>(`${Env.ApiUrl}/${ApiPaths.QuestionOptions}/${questionOption.id}/`, questionOption);
  }

  public removeQuestionOption(questionOption: QuestionOption) {
    return this.httpClient.delete<JSON>(`${Env.ApiUrl}/${ApiPaths.QuestionOptions}/${questionOption.id}/`);
  }
}
