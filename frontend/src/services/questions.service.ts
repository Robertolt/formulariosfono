import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { ApiPaths } from 'src/data/api-paths';
import { Env } from 'src/data/env';
import { Question } from 'src/models/question';

@Injectable({
  providedIn: 'root'
})
export class QuestionsService {
  constructor(private httpClient: HttpClient) { }

  public createQuestion(questionnarieId: number) {
    let question: Question = new Question();

    question.questionnaire = questionnarieId;
    question.text = "Nova questão";
    question.question_type = "RD";

    return this.httpClient.post<JSON>(`${Env.ApiUrl}/${ApiPaths.Questions}/`, question);
  }

  public getQuestion(id: number) {
    return this.httpClient.get<JSON>(`${Env.ApiUrl}/${ApiPaths.Questions}/${id}/`);
  }

  public updateQuestion(question: Question) {
    return this.httpClient.put<JSON>(`${Env.ApiUrl}/${ApiPaths.Questions}/${question.id}/`, question);
  }

  public removeQuestion(question: any) {
    return this.httpClient.delete<JSON>(`${Env.ApiUrl}/${ApiPaths.Questions}/${question.id}/`);
  }
}
