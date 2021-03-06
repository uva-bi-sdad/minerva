function startDiscussIntro() {   
    var intro = introJs();
//    intro.setOption('exitOnOverlayClick', false);
//    intro.setOption('exitOnEsc', false);
    intro.setOption('showStepNumbers', false);
    intro.setOption('skipLabel', '');
    intro.addSteps([
      {
        element: document.querySelectorAll('#playerDiv')[0],
        intro: "In each round, you will be assigned a randomly chosen <strong>identity (or avatar)</strong> and a <strong>threshold T</strong>. " +
               "In this example above, your avatar is <strong>Cow</strong> and your <strong>threshold T=1</strong>. " +
               "<br><br>In each round, every player will be assigned a new avatar and a new threshold.",
      },
      {
        element: document.querySelectorAll('#reward-summary')[0],
        intro: "Here you can see the possible earnings for the round.",
      },
      {
        element: document.querySelectorAll('#friendsDiv')[0],
        intro: "In each round, you will be connected to some or all of the other players in your group. They will be called <strong>your friends</strong>. " +
               "Here, you will see your friends and their thresholds. " +
               "<br><br>You can <strong>click on your friends' avatars</strong> to see their page, their friends, and their friends' thresholds. " +
               "<br><br>You can <strong>post messages</strong> on your friends’ walls.",
      },
      {
        element: document.querySelectorAll('.container-network')[0],
        intro: "This diagram shows <strong>your network</strong> for the round: your connections (friends) in the group. " +
               "There is a gray line between your avatar and each of your friends' avatars. " +
               "<br><br>You can observe your connections in this box, but you cannot observe the connections between your friends or other players. " +
               "The shape of the network may or may not be the same in each round.",
      },
      {
        element: document.querySelectorAll('.container-groupList')[0],
        intro: "These are all of the players in your group. Some or all of them are in your list of friends. " +
               "When a player moves on to the next page and is waiting for you, it will be displayed here. ",
      },
      {
        element: document.querySelectorAll('.message-tool')[0],
        intro: "In the <strong>messaging part</strong>, you can use this tool to post messages " +
               "revealing your intention to participate or not in the group event. " +
               "<br><br>You can post: <strong>1) 'I will participate'</strong>, <strong>2) 'I will not participate'</strong> or choose <strong>'no messages</strong> for the round. " +
               "<br><br>Each player can post a message on his/her own wall and friends' walls. " +
               "Posts on a player's wall can be viewed by all of his/her friends. " +
               "<br><br>Try using the messaging tool by selecting the recipient and a message (from the dropdown menu). " +
               "You will click 'Submit' to post your messages in the actual game.",        
        position: "top",
        disableInteraction: false,
        position: "right",
      },
      {
        element: document.querySelectorAll('.wall-card')[0],
        intro: "Every player has a <strong>wall</strong>, where messages can be posted and viewed by friends. " +
               "The messages on your wall and on your friends' walls will be received and viewed in the <strong>decision part</strong>.",
        //position: "top",
      },
      {
        element: document.querySelectorAll('#stopButton')[0],
        intro: "Once you are done with posting messages, you can click 'Next' to proceed to the decision part. " +
               "You cannot post messages in the decision part.",
        disableInteraction: true,
      },
      /*
      {
        element: document.querySelectorAll('#stopModal-content')[0],
        intro: "You can review your posts and click “Edit” to make changes: you can remove existing messages or post new ones. " +
               "Make sure that you post all of the messages you want before clicking 'Continue' as you cannot get back to the messaging part.  " +
               "When you click 'Continue', you will proceed to the decision part.",
        disableInteraction: true,
      },
      {
        element: document.querySelectorAll('.next-button')[0],
        intro: "<h5><em><strong>Please click Continue to move to the tour of the decision part.</strong></em><h5>",
      },
      */
    ]);
    intro.onchange(function(targetElement) {   
        if (targetElement.id == 'stopModal-content') 
            { 
                $('#stopModal-content').css('display','inline-block');
            }
        if (targetElement.id == 'stopButton') 
            { 
                $('#stopModal-content').css('display','none');
            }
        });
    intro.start();
  }
  
  
  function startDecideIntro() {   
    var intro = introJs();
//    intro.setOption('exitOnOverlayClick', false);
//    intro.setOption('exitOnEsc', false);
    intro.setOption('showStepNumbers', false);
    intro.setOption('skipLabel', '');
    intro.addSteps([
      {
        element: document.querySelectorAll('.wall-card')[0],
        intro: "In the decision part, each player can observe the messages posted on their own walls and on their friends' walls. " +
               "You will not be able to post or receive any more messages. ",
        position: "top",
      },
      {
        element: document.querySelectorAll('#friendsDiv')[0],
        intro: "You can click on your friends' avatars to view the messages posted on their walls by their friends.",  
      }, 
      {
        element: document.querySelectorAll('#participate-group')[0],
        intro: "After reviewing the messages, each player in the group then must decide whether <strong>to participate</strong> or <strong>not " +
               "participate</strong> for this round. After making your participation decision for the round, a new round will start. You will not observe the outcome of the rounds. " +
               "<br><br>After you play all the rounds, we will choose a random round and you will be paid based on the " +
               "result of that round. Because each round has the same chance of being chosen for payment, you should pay careful attention to " +
               "each round.",
      },
      /*
      {
        element: document.querySelectorAll('#help-nav')[0],
        intro: "At any time, you can view the instructions, this tour and the quiz.",
      },
      {
        element: document.querySelectorAll('.next-button')[0],
        intro: "Next, you will have 3 practice rounds before the actual game starts. <br/><br/><h5><em><strong>Please click 'Continue' now.</strong></em><h5/>",
      },
      */
    ]);
     
    intro.start();
  }
