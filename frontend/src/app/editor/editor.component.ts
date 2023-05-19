import { Component } from '@angular/core';
import { ActivatedRoute } from '@angular/router';
import { Question } from 'src/models/question';
import { Questionnaire } from 'src/models/questionnaire';
import { QuestionnariesService } from 'src/services/questionnaries.service';
import { QuestionsService } from 'src/services/questions.service';

@Component({
  selector: 'app-editor',
  templateUrl: './editor.component.html',
  styleUrls: ['./editor.component.css']
})
export class EditorComponent {
  questionnaire: Questionnaire = new Questionnaire();

  constructor(
    private route: ActivatedRoute,
    private questionnariesService: QuestionnariesService,
    private questionsService: QuestionsService) {
  }

  ngOnInit() {
    // First get the product id from the current route.
    const routeParams = this.route.snapshot.paramMap;
    const questionnarieIdFromRoute: number = Number(routeParams.get('questionnarieId'));

    this.questionnariesService.getQuestionnarie(questionnarieIdFromRoute).subscribe((data: any) => {
      this.questionnaire = data;
    });
  }

  handleNewQuestionClick() {
    this.questionsService.createQuestion(this.questionnaire.id).subscribe((data: any) => {
      this.questionnaire.question_set.push(data.id);
    });
  }

  updateQuestionnaire() {
    this.questionnariesService.updateQuestionnarie(this.questionnaire).subscribe((data: any) => {
      this.questionnaire = data;
    });
  }

  handleQuestionRemoved(questionId: number) {
    this.questionnaire.question_set = this.questionnaire.question_set.filter(q => q !== questionId);
  }
}
