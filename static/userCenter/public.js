var isShowExplainImg=true;
$(function(){
	isShowExplainImgf();
});
function isShowExplainImgf(){
	if(isShowExplainImg){
		$("[name='showExplainImg']").show();
//		$('body').on('click', '.close', function () {
//		    $('body').removeAttr("style");
//		    $('.mengc').remove()
//		});
	}
}
function close_box_body(){
	 $('body').removeAttr("style");
	 $('.mengc').remove();
}
function showExplain(val) {
	event.stopPropagation();
    console.log(val);
    // 文字信息复制
    let str = '';
    switch (val) {
      case 1:
        str = '未发生《风险提示函》项下风险且《借款协议》及相关协议正常履行完毕后，期望获得的回报与出借（或受让）本金的比率，据此换算成的年化回报率。期望年化回报率仅供参考，不代表实际回报。'
        break;
      case 2:
        str = '根据监管法规要求，借贷双方自主签约，出借期限以借款协议期限为准，根据借款标的情况，最长借款期限为48个月。封闭期内，用户不得转让债权。封闭期届满后，用户可以申请自主转让债权或者授权平台通过系统提交转让申请信息，平台仅提供转让信息撮合服务，不参与也不保证转让成功的时间与价格，用户不得因转让效率和成功率向平台追责，完全由市场决定。如用户债权转让未达成，用户需继续持有债权直至对应借款协议到期（如对应借款协议剩余48个月，则无论封闭期多久需要持有到48个月满），若借款协议期满借款人仍未还款的，则继续持有债权直至债权因借款人还款或第三方代偿导致债权结束。'
        break;
      case 3:
        str = '总资产=活动资金+您购买产品的金额；总资产意味着您雄厚的资本，以及给您盈利的能力'
        break;
      case 4:
          str = '指定期望转让成功日期系用户选择的期望转让成功时间，并非平台承诺债权转出以及资金到账的承诺日期，回款到账时间以及金额受流动性风险（债权履约情况）以及银行支付等因素影响，可能有所延迟。玖富普惠将尽力为您寻找债权受让方，若债权未能及时足额转出，您将继续持有该债权'
          break;
      case 5:
          str = '该笔订单截止到今日累计还款或转让总额（扣除服务费等）该金额由理财后台提供'
          break;
      case 6:
          str = '该笔订单对应的所有债权当前公允价值总和，每天会发生变化该金额由理财后台提供'
          break;
      case 7:
          str = '根据监管法规要求，借贷双方自主签约，出借期限以借款协议期限为准，根据借款标的情况，最长借款期限为48个月。封闭期内，用户不得转让债权。封闭期届满后，用户可以申请自主转让债权或者授权平台通过系统提交转让申请信息，平台仅提供转让信息撮合服务，不参与也不保证转让成功的时间与价格，用户不得因转让效率和成功率向平台追责，完全由市场决定。如用户债权转让未达成，用户需继续持有债权直至对应借款协议到期（如对应借款协议剩余48个月，则无论封闭期多久需要持有到48个月满），若借款协议期满借款人仍未还款的，则继续持有债权直至债权因借款人还款或第三方代偿导致债权结束。'
          break;
      case 8:
          str = '依据当前的债权价值计算得出，订单状态的变化可能会影响资产总额的变化'
          break;
      case 9:
          str = '封闭期不同于出借期限，出借期限与借款人签署的借款协议期限完全匹配，根据借款标的情况，最长借款期限为48个月，出借人可能持有借款期限最长的债权直至借款期限届满。';
      case 10:
          str = '今日盈利：这个数字就是在今天3点之前，你的预期盈利，会出现在你指定的账户中，记得及时查看。';
      default:
    }

    var mengc = $('<div class="mengc"></div>').css({
      "box-sizing": "border-box",
      "position": "fixed",
      "top": "0",
      "bottom": "0",
      "width": "100%",
      "padding-left": ".7rem",
      "padding-right": ".7rem",
      "background-color": "rgba(0, 0, 0, .5)",
      "z-index": "9999",
      "font-size": '.24rem'
    })
    var tkbox = $('<div class="tk-box"></div>').css({
      "position": "relative",
      "top": "3.2rem",
      "box-sizing": "border-box",
      "width": "100%",
      "background-color": "#fff",
      "padding": ".5rem .31rem .5rem .3rem",
      "border-radius": ".2rem"
    }).html(str)
    var close = $("<div class='close' onclick='close_box_body()' ></div>").css({
      "width": ".66rem",
      "height": ".66rem",
      "border": "solid 1px #fff",
      "border-radius": "50%",
      "position": "absolute",
      "left": "50%",
      "bottom": "-1.1rem",
      "margin-left": "-.33rem"
    })
    var before = $('<div class = "before"></div>').css({
      "position": "absolute",
      "height": "1px",
      "width": ".4rem",
      "top": ".32rem",
      "left": ".13rem",
      "background-color": " #fff",
      "transform": "rotate(45deg)"
    })
    var after = $('<div class = "after"></div>').css({
      "position": "absolute",
      "height": "1px",
      "width": ".4rem",
      "top": ".32rem",
      "left": ".13rem",
      "background-color": " #fff",
      "transform": "rotate(-45deg)"
    })
    close.append(before).append(after)
    mengc.append(tkbox.append(close))
    console.log(mengc)
    $('body').append(mengc)
    $('body').css({
      overflow: 'hidden',
      height: $(window).height() + 'px'
    })
  }

