import { Component, Input, Output, EventEmitter } from '@angular/core';
import { Question } from 'src/models/question';
import { QuestionsService } from 'src/services/questions.service';
import { QuestionOptionsService } from 'src/services/question-options.service';

@Component({
  selector: 'app-radio-editor',
  templateUrl: './radio-editor.component.html',
  styleUrls: ['./radio-editor.component.css']
})
export class RadioEditorComponent {
  @Input() questionId: number = 0;
  @Input() numberInQuestionnarie: number = 0;
  @Output() questionChange = new EventEmitter<Question>();
  @Output() onQuestionRemove = new EventEmitter<number>();

  question: Question = new Question();

  constructor(
    private questionsService: QuestionsService,
    private questionOptionsService: QuestionOptionsService) {
  }

  ngOnInit() {
    this.questionsService.getQuestion(this.questionId).subscribe((data: any) => {
      this.question = data;
    });
  }

  updateQuestion() {
    this.questionsService.updateQuestion(this.question).subscribe((data: any) => {
      this.question = data;
    });
  }

  addNewOption() {
    this.questionOptionsService.createQuestionOption(this.question.id).subscribe((data: any) => {
      this.question.question_option_set.push(data.id);
    });
  }

  removeOption(id: number) {
    this.question.question_option_set = this.question.question_option_set.filter(option => option !== id);
  }

  removeQuestion() {
    const isOkDelete: boolean = confirm('Tem certeza que deseja remover a questão e todas as suas opções?');

    if (isOkDelete) {
      this.questionsService.removeQuestion(this.question).subscribe((data: any) => {
        this.onQuestionRemove.emit(this.question.id);
      });
    }
  }
}
