import { Component, Input, Output, EventEmitter } from '@angular/core';
import { QuestionOption } from 'src/models/question_option';
import { QuestionOptionsService } from 'src/services/question-options.service';

@Component({
  selector: 'app-radio-answer',
  templateUrl: './radio-answer.component.html',
  styleUrls: ['./radio-answer.component.css']
})
export class RadioAnswerComponent {
  @Input() optionId: number = 0;
  @Output() optionChange = new EventEmitter<QuestionOption>();
  @Output() onOptionRemove = new EventEmitter<number>();

  questionOption: QuestionOption = new QuestionOption();

  constructor(
    private optionsService: QuestionOptionsService) {
  }

  ngOnInit() {
    this.optionsService.getQuestionOption(this.optionId).subscribe((data: any) => {
      this.questionOption = data;
    });
  }

  updateQuestionOption() {
    this.optionsService.updateQuestionOption(this.questionOption).subscribe((data: any) => {
      this.questionOption = data;
    });
  }

  removeQuestionOption() {
    let optionRemoved = this.questionOption.id;
    this.optionsService.removeQuestionOption(this.questionOption).subscribe((data: any) => {
      this.onOptionRemove.emit(optionRemoved);
    });
  }
}
