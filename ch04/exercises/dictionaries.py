short_article = " Today, at an event at the White House, President Biden sought to draw contrasts between Democratic and Republican policies affecting seniors, suggesting his party is committed to lowering health-care costs while raising fears that GOP plans could jeopardize Medicare and Social Security. With the midterms looming, Biden took aim at three GOP lawmakers by name who he said are putting forward suspect plans: House Minority Leader Kevin McCarthy (Calif.) and Sens. Rick Scott (Fla.) and Ron Johnson (Wis.). The speech had been scheduled for delivery in Florida as part of a trip that was canceled because of Hurricane Ian. Also ahead of the hurricane’s landfall in Florida, the House committee investigating the Jan. 6, 2021, attack on the Capitol postponed its Wednesday hearing, committee leaders announced."

substitutions = {"White House":"Pit of Despair",
  "allegedly":"totally",
  "bill":"snap I didn’t screenshot",
  "official":"puppy",
  "congressional":"spaaaaace",
  "republican":"piano accordionist",
  "democrat":"chromatic button accordionist",
  "senator": "magical wizard",
  "representative": "unmagical wizard",
  "secretary":"eating champion",
  "leaders":"goblins",
  "washington":"Mount Doom",
  "president": "you know, the guy",
  "I" : "you"}


for key, value in substitutions.items():
  short_article = short_article.replace(key,value)

print(short_article)