---
name: indicator-development-skill
description: Master custom indicator development for all trading platforms. Use for MetaTrader indicators (MQL4/MQL5), TradingView Pine Script indicators, Python technical analysis (TA-Lib, Pandas), custom oscillators, trend indicators, volume indicators, multi-timeframe indicators, repainting prevention, alert systems, webhook integrations, indicator optimization, visual customization, and creating production-ready technical indicators for Forex, Crypto, and Stocks.
---

# 📊 Indicator Development Mastery Skill

> **Master custom indicator development across all platforms**
>
> **Platforms:** MetaTrader 4/5 | TradingView | Python
>
> **Categories:** Trend | Oscillators | Volume | Custom

---

## 📚 Table of Contents

1. [Indicator Fundamentals](#indicator-fundamentals)
2. [MetaTrader Indicators (MQL4/MQL5)](#metatrader-indicators)
3. [TradingView Pine Script Indicators](#tradingview-indicators)
4. [Python Custom Indicators](#python-indicators)
5. [Popular Indicator Library](#popular-indicators)
6. [Multi-Timeframe Indicators](#multi-timeframe)
7. [Alert Systems & Webhooks](#alerts-webhooks)
8. [Repainting Prevention](#repainting-prevention)
9. [Performance Optimization](#performance-optimization)
10. [Visualization & UI](#visualization)

---

## 1. Indicator Fundamentals {#indicator-fundamentals}

### 🎯 Indicator Categories

**1. Trend Indicators** (Direction)
```
✅ Moving Averages (SMA, EMA, WMA)
✅ MACD (Moving Average Convergence Divergence)
✅ Parabolic SAR
✅ ADX (Average Directional Index)
✅ Ichimoku Cloud
✅ Supertrend
```

**2. Oscillators** (Momentum)
```
✅ RSI (Relative Strength Index)
✅ Stochastic Oscillator
✅ CCI (Commodity Channel Index)
✅ Williams %R
✅ Momentum Indicator
✅ ROC (Rate of Change)
```

**3. Volatility Indicators**
```
✅ ATR (Average True Range)
✅ Bollinger Bands
✅ Keltner Channels
✅ Donchian Channels
✅ Standard Deviation
```

**4. Volume Indicators**
```
✅ Volume Weighted Average Price (VWAP)
✅ On-Balance Volume (OBV)
✅ Volume Profile
✅ Money Flow Index (MFI)
✅ Accumulation/Distribution
```

---

## 2. MetaTrader Indicators (MQL4/MQL5) {#metatrader-indicators}

### 🎯 MQL4 Indicator Template

```mql4
//+------------------------------------------------------------------+
//|                                           Custom_RSI.mq4         |
//|                                    Custom RSI with Alerts        |
//+------------------------------------------------------------------+

#property indicator_separate_window
#property indicator_buffers 1
#property indicator_color1 Blue
#property indicator_level1 30
#property indicator_level2 50
#property indicator_level3 70
#property indicator_minimum 0
#property indicator_maximum 100

// Input Parameters
input int RSI_Period = 14;
input ENUM_APPLIED_PRICE RSI_Price = PRICE_CLOSE;
input bool EnableAlerts = true;

// Indicator Buffers
double RSI_Buffer[];

// Global Variables
datetime lastAlertTime = 0;

//+------------------------------------------------------------------+
//| Custom indicator initialization                                  |
//+------------------------------------------------------------------+
int OnInit()
{
   // Set buffer as indicator line
   SetIndexBuffer(0, RSI_Buffer);
   SetIndexStyle(0, DRAW_LINE, STYLE_SOLID, 2);
   SetIndexLabel(0, "Custom RSI");

   // Indicator name
   IndicatorShortName("Custom RSI(" + IntegerToString(RSI_Period) + ")");

   return(INIT_SUCCEEDED);
}

//+------------------------------------------------------------------+
//| Custom indicator iteration                                       |
//+------------------------------------------------------------------+
int OnCalculate(const int rates_total,
                const int prev_calculated,
                const datetime &time[],
                const double &open[],
                const double &high[],
                const double &low[],
                const double &close[],
                const long &tick_volume[],
                const long &volume[],
                const int &spread[])
{
   // Calculate starting position
   int start = prev_calculated - 1;
   if(start < RSI_Period)
      start = RSI_Period;

   // Calculate RSI for each bar
   for(int i = start; i < rates_total; i++)
   {
      RSI_Buffer[i] = iRSI(NULL, 0, RSI_Period, RSI_Price, i);

      // Check for alerts on most recent bar
      if(i == rates_total - 1 && EnableAlerts)
      {
         CheckAlerts(RSI_Buffer[i], time[i]);
      }
   }

   return(rates_total);
}

//+------------------------------------------------------------------+
//| Check alert conditions                                           |
//+------------------------------------------------------------------+
void CheckAlerts(double rsi_value, datetime current_time)
{
   // Prevent multiple alerts on same bar
   if(current_time == lastAlertTime)
      return;

   // Oversold alert
   if(rsi_value < 30)
   {
      Alert("RSI Oversold: ", DoubleToString(rsi_value, 2));
      lastAlertTime = current_time;
   }
   // Overbought alert
   else if(rsi_value > 70)
   {
      Alert("RSI Overbought: ", DoubleToString(rsi_value, 2));
      lastAlertTime = current_time;
   }
}
```

### 🎯 MQL5 Multi-Buffer Indicator (MACD)

```mql5
//+------------------------------------------------------------------+
//|                                              Custom_MACD.mq5     |
//+------------------------------------------------------------------+

#property indicator_separate_window
#property indicator_buffers 3
#property indicator_plots   2

// Plot settings
#property indicator_label1  "MACD"
#property indicator_type1   DRAW_LINE
#property indicator_color1  clrBlue
#property indicator_style1  STYLE_SOLID
#property indicator_width1  2

#property indicator_label2  "Signal"
#property indicator_type2   DRAW_LINE
#property indicator_color2  clrRed
#property indicator_style2  STYLE_SOLID
#property indicator_width2  1

// Input Parameters
input int FastEMA = 12;
input int SlowEMA = 26;
input int SignalSMA = 9;
input ENUM_APPLIED_PRICE AppliedPrice = PRICE_CLOSE;

// Indicator Buffers
double MacdBuffer[];
double SignalBuffer[];
double HistogramBuffer[];

// Handles
int fastHandle, slowHandle;

//+------------------------------------------------------------------+
//| Custom indicator initialization                                  |
//+------------------------------------------------------------------+
int OnInit()
{
   // Set buffers
   SetIndexBuffer(0, MacdBuffer, INDICATOR_DATA);
   SetIndexBuffer(1, SignalBuffer, INDICATOR_DATA);
   SetIndexBuffer(2, HistogramBuffer, INDICATOR_CALCULATIONS);

   // Create EMA handles
   fastHandle = iMA(_Symbol, PERIOD_CURRENT, FastEMA, 0, MODE_EMA, AppliedPrice);
   slowHandle = iMA(_Symbol, PERIOD_CURRENT, SlowEMA, 0, MODE_EMA, AppliedPrice);

   if(fastHandle == INVALID_HANDLE || slowHandle == INVALID_HANDLE)
   {
      Print("Error creating MA handles");
      return(INIT_FAILED);
   }

   // Indicator name
   IndicatorSetString(INDICATOR_SHORTNAME, "MACD(" +
                      IntegerToString(FastEMA) + "," +
                      IntegerToString(SlowEMA) + "," +
                      IntegerToString(SignalSMA) + ")");

   return(INIT_SUCCEEDED);
}

//+------------------------------------------------------------------+
//| Custom indicator iteration                                       |
//+------------------------------------------------------------------+
int OnCalculate(const int rates_total,
                const int prev_calculated,
                const datetime &time[],
                const double &open[],
                const double &high[],
                const double &low[],
                const double &close[],
                const long &tick_volume[],
                const long &volume[],
                const int &spread[])
{
   // Calculate starting position
   int start = prev_calculated - 1;
   if(start < SlowEMA + SignalSMA)
      start = SlowEMA + SignalSMA;

   // Get EMA values
   double fastEMA[], slowEMA[];
   ArraySetAsSeries(fastEMA, true);
   ArraySetAsSeries(slowEMA, true);

   if(CopyBuffer(fastHandle, 0, 0, rates_total, fastEMA) <= 0)
      return(0);
   if(CopyBuffer(slowHandle, 0, 0, rates_total, slowEMA) <= 0)
      return(0);

   // Calculate MACD
   for(int i = start; i < rates_total; i++)
   {
      MacdBuffer[i] = fastEMA[i] - slowEMA[i];
   }

   // Calculate Signal line (SMA of MACD)
   for(int i = start; i < rates_total; i++)
   {
      double sum = 0;
      for(int j = 0; j < SignalSMA; j++)
      {
         sum += MacdBuffer[i - j];
      }
      SignalBuffer[i] = sum / SignalSMA;
   }

   // Calculate Histogram (for potential use)
   for(int i = start; i < rates_total; i++)
   {
      HistogramBuffer[i] = MacdBuffer[i] - SignalBuffer[i];
   }

   return(rates_total);
}

//+------------------------------------------------------------------+
//| Cleanup                                                          |
//+------------------------------------------------------------------+
void OnDeinit(const int reason)
{
   IndicatorRelease(fastHandle);
   IndicatorRelease(slowHandle);
}
```

---

## 3. TradingView Pine Script Indicators {#tradingview-indicators}

### 🎯 Custom RSI with Multiple Levels

```pinescript
//@version=5
indicator("Custom RSI Pro", overlay=false, timeframe="", timeframe_gaps=true)

// ==================== INPUTS ====================
rsiLength = input.int(14, "RSI Length", minval=1)
rsiSource = input.source(close, "RSI Source")
smoothK = input.int(3, "Stochastic %K Smoothing", minval=1)
smoothD = input.int(3, "Stochastic %D Smoothing", minval=1)

// Levels
level90 = input.int(90, "Extreme Overbought", group="Levels")
level70 = input.int(70, "Overbought", group="Levels")
level50 = input.int(50, "Midline", group="Levels")
level30 = input.int(30, "Oversold", group="Levels")
level10 = input.int(10, "Extreme Oversold", group="Levels")

// Colors
colorOverbought = input.color(color.red, "Overbought Color", group="Colors")
colorOversold = input.color(color.green, "Oversold Color", group="Colors")
colorNeutral = input.color(color.gray, "Neutral Color", group="Colors")

// ==================== CALCULATIONS ====================
// Calculate RSI
rsi = ta.rsi(rsiSource, rsiLength)

// Stochastic RSI
rsiLowest = ta.lowest(rsi, smoothK)
rsiHighest = ta.highest(rsi, smoothK)
stochRSI = (rsi - rsiLowest) / (rsiHighest - rsiLowest) * 100
k = ta.sma(stochRSI, smoothD)
d = ta.sma(k, smoothD)

// ==================== DYNAMIC COLORING ====================
rsiColor = rsi > level70 ? colorOverbought :
           rsi < level30 ? colorOversold :
           colorNeutral

// ==================== PLOTTING ====================
// Main RSI line
plot(rsi, "RSI", color=rsiColor, linewidth=2)

// Stochastic RSI (optional, commented out by default)
// plot(k, "Stoch %K", color=color.blue)
// plot(d, "Stoch %D", color=color.orange)

// Horizontal levels
hline(level90, "Extreme OB", color=color.new(color.red, 70), linestyle=hline.style_dotted)
hline(level70, "Overbought", color=color.new(color.red, 50), linestyle=hline.style_dashed)
hline(level50, "Midline", color=color.gray, linestyle=hline.style_solid)
hline(level30, "Oversold", color=color.new(color.green, 50), linestyle=hline.style_dashed)
hline(level10, "Extreme OS", color=color.new(color.green, 70), linestyle=hline.style_dotted)

// ==================== DIVERGENCE DETECTION ====================
// Bullish divergence: Price makes lower low, RSI makes higher low
pivotLowPrice = ta.pivotlow(close, 5, 5)
pivotLowRSI = ta.pivotlow(rsi, 5, 5)

bullishDiv = false
if not na(pivotLowPrice) and not na(pivotLowRSI)
    bullishDiv := close < close[10] and rsi > rsi[10]

// Bearish divergence: Price makes higher high, RSI makes lower high
pivotHighPrice = ta.pivothigh(close, 5, 5)
pivotHighRSI = ta.pivothigh(rsi, 5, 5)

bearishDiv = false
if not na(pivotHighPrice) and not na(pivotHighRSI)
    bearishDiv := close > close[10] and rsi < rsi[10]

// Plot divergence signals
plotshape(bullishDiv, "Bullish Div", shape.triangleup, location.absolute, color.green, size=size.small, text="BD")
plotshape(bearishDiv, "Bearish Div", shape.triangledown, location.absolute, color.red, size=size.small, text="BD")

// ==================== ALERTS ====================
alertcondition(ta.crossover(rsi, level70), "RSI Overbought", "RSI crossed above 70")
alertcondition(ta.crossunder(rsi, level30), "RSI Oversold", "RSI crossed below 30")
alertcondition(bullishDiv, "Bullish Divergence", "Bullish divergence detected")
alertcondition(bearishDiv, "Bearish Divergence", "Bearish divergence detected")

// ==================== BACKGROUND COLORING ====================
bgcolor(rsi > level90 ? color.new(color.red, 90) :
        rsi < level10 ? color.new(color.green, 90) : na)
```

### 🎯 Custom Supertrend Indicator

```pinescript
//@version=5
indicator("Supertrend Pro", overlay=true)

// ==================== INPUTS ====================
atrPeriod = input.int(10, "ATR Period", minval=1)
atrMultiplier = input.float(3.0, "ATR Multiplier", minval=0.5, step=0.1)
changeATR = input.bool(true, "Change ATR Calculation Method")

// ==================== CALCULATIONS ====================
// ATR Calculation
atr = ta.atr(atrPeriod)

// Upper and Lower Bands
upperBand = hl2 + (atrMultiplier * atr)
lowerBand = hl2 - (atrMultiplier * atr)

// Supertrend Logic
var float supertrend = na
var int direction = 1  // 1 = uptrend, -1 = downtrend

// Previous values
prevUpperBand = nz(upperBand[1], upperBand)
prevLowerBand = nz(lowerBand[1], lowerBand)
prevSupertrend = nz(supertrend[1], lowerBand)
prevDirection = nz(direction[1], 1)

// Update bands
if close[1] > prevUpperBand
    lowerBand := math.max(lowerBand, prevLowerBand)
if close[1] < prevLowerBand
    upperBand := math.min(upperBand, prevUpperBand)

// Determine trend direction
if prevDirection == 1
    direction := close > prevSupertrend ? 1 : -1
else
    direction := close < prevSupertrend ? -1 : 1

// Set supertrend value
supertrend := direction == 1 ? lowerBand : upperBand

// ==================== TREND CHANGES ====================
trendUp = direction == 1 and prevDirection == -1
trendDown = direction == -1 and prevDirection == 1

// ==================== PLOTTING ====================
// Plot supertrend
plot(supertrend, "Supertrend", color=direction == 1 ? color.green : color.red, linewidth=2)

// Buy/Sell signals
plotshape(trendUp, "Buy Signal", shape.triangleup, location.belowbar, color.green, size=size.normal)
plotshape(trendDown, "Sell Signal", shape.triangledown, location.abovebar, color.red, size=size.normal)

// Background color
bgcolor(direction == 1 ? color.new(color.green, 95) : color.new(color.red, 95))

// ==================== ALERTS ====================
alertcondition(trendUp, "Supertrend Buy", "Supertrend changed to UPTREND")
alertcondition(trendDown, "Supertrend Sell", "Supertrend changed to DOWNTREND")
```

---

## 4. Python Custom Indicators {#python-indicators}

### 🎯 Custom Indicator Class Template

```python
import pandas as pd
import numpy as np
import talib as ta

class CustomIndicator:
    """
    Base class for custom indicators
    """

    def __init__(self, df):
        """
        Initialize with OHLCV dataframe
        df columns: ['open', 'high', 'low', 'close', 'volume']
        """
        self.df = df.copy()

    def calculate_rsi(self, period=14, column='close'):
        """Calculate RSI indicator"""
        delta = self.df[column].diff()
        gain = (delta.where(delta > 0, 0)).rolling(window=period).mean()
        loss = (-delta.where(delta < 0, 0)).rolling(window=period).mean()

        rs = gain / loss
        rsi = 100 - (100 / (1 + rs))

        self.df[f'rsi_{period}'] = rsi
        return rsi

    def calculate_macd(self, fast=12, slow=26, signal=9, column='close'):
        """Calculate MACD indicator"""
        exp1 = self.df[column].ewm(span=fast, adjust=False).mean()
        exp2 = self.df[column].ewm(span=slow, adjust=False).mean()

        macd = exp1 - exp2
        signal_line = macd.ewm(span=signal, adjust=False).mean()
        histogram = macd - signal_line

        self.df['macd'] = macd
        self.df['macd_signal'] = signal_line
        self.df['macd_histogram'] = histogram

        return macd, signal_line, histogram

    def calculate_bollinger_bands(self, period=20, std_dev=2, column='close'):
        """Calculate Bollinger Bands"""
        sma = self.df[column].rolling(window=period).mean()
        std = self.df[column].rolling(window=period).std()

        upper_band = sma + (std * std_dev)
        lower_band = sma - (std * std_dev)

        self.df['bb_upper'] = upper_band
        self.df['bb_middle'] = sma
        self.df['bb_lower'] = lower_band
        self.df['bb_width'] = upper_band - lower_band

        return upper_band, sma, lower_band

    def calculate_atr(self, period=14):
        """Calculate Average True Range"""
        high = self.df['high']
        low = self.df['low']
        close = self.df['close']

        tr1 = high - low
        tr2 = abs(high - close.shift())
        tr3 = abs(low - close.shift())

        tr = pd.concat([tr1, tr2, tr3], axis=1).max(axis=1)
        atr = tr.rolling(window=period).mean()

        self.df[f'atr_{period}'] = atr
        return atr

    def calculate_stochastic(self, k_period=14, d_period=3):
        """Calculate Stochastic Oscillator"""
        low_min = self.df['low'].rolling(window=k_period).min()
        high_max = self.df['high'].rolling(window=k_period).max()

        k = 100 * ((self.df['close'] - low_min) / (high_max - low_min))
        d = k.rolling(window=d_period).mean()

        self.df['stoch_k'] = k
        self.df['stoch_d'] = d

        return k, d

    def calculate_adx(self, period=14):
        """Calculate ADX (Average Directional Index)"""
        high = self.df['high']
        low = self.df['low']
        close = self.df['close']

        plus_dm = high.diff()
        minus_dm = low.diff()

        plus_dm[plus_dm < 0] = 0
        minus_dm[minus_dm > 0] = 0

        atr = self.calculate_atr(period)

        plus_di = 100 * (plus_dm.ewm(alpha=1/period).mean() / atr)
        minus_di = abs(100 * (minus_dm.ewm(alpha=1/period).mean() / atr))

        dx = (abs(plus_di - minus_di) / abs(plus_di + minus_di)) * 100
        adx = dx.ewm(alpha=1/period).mean()

        self.df['adx'] = adx
        self.df['plus_di'] = plus_di
        self.df['minus_di'] = minus_di

        return adx

    def calculate_vwap(self):
        """Calculate Volume Weighted Average Price"""
        typical_price = (self.df['high'] + self.df['low'] + self.df['close']) / 3
        vwap = (typical_price * self.df['volume']).cumsum() / self.df['volume'].cumsum()

        self.df['vwap'] = vwap
        return vwap

    def detect_rsi_divergence(self, rsi_column='rsi_14', lookback=5):
        """
        Detect RSI divergence
        Returns: bullish_div, bearish_div (boolean series)
        """
        # Price pivots
        price_pivot_low = self.df['low'].rolling(window=lookback*2+1, center=True).min() == self.df['low']
        price_pivot_high = self.df['high'].rolling(window=lookback*2+1, center=True).max() == self.df['high']

        # RSI pivots
        rsi_pivot_low = self.df[rsi_column].rolling(window=lookback*2+1, center=True).min() == self.df[rsi_column]
        rsi_pivot_high = self.df[rsi_column].rolling(window=lookback*2+1, center=True).max() == self.df[rsi_column]

        # Bullish divergence: Price lower low, RSI higher low
        bullish_div = (
            price_pivot_low &
            (self.df['low'] < self.df['low'].shift(lookback)) &
            (self.df[rsi_column] > self.df[rsi_column].shift(lookback))
        )

        # Bearish divergence: Price higher high, RSI lower high
        bearish_div = (
            price_pivot_high &
            (self.df['high'] > self.df['high'].shift(lookback)) &
            (self.df[rsi_column] < self.df[rsi_column].shift(lookback))
        )

        self.df['bullish_divergence'] = bullish_div
        self.df['bearish_divergence'] = bearish_div

        return bullish_div, bearish_div

    def calculate_all(self):
        """Calculate all indicators at once"""
        self.calculate_rsi()
        self.calculate_macd()
        self.calculate_bollinger_bands()
        self.calculate_atr()
        self.calculate_stochastic()
        self.calculate_adx()
        self.calculate_vwap()
        self.detect_rsi_divergence()

        return self.df


# ==================== USAGE EXAMPLE ====================
if __name__ == '__main__':
    # Sample data
    df = pd.DataFrame({
        'open': [100, 102, 101, 103, 105],
        'high': [103, 104, 104, 106, 108],
        'low': [99, 101, 100, 102, 104],
        'close': [102, 103, 102, 105, 107],
        'volume': [1000, 1200, 900, 1500, 1800]
    })

    # Calculate indicators
    indicator = CustomIndicator(df)
    result_df = indicator.calculate_all()

    print(result_df)
```

---

## 5. Popular Indicator Library {#popular-indicators}

### 🎯 Quick Reference Guide

**1. RSI (Relative Strength Index)**
```
Purpose: Overbought/oversold conditions
Range: 0-100
Signals:
- RSI > 70 = Overbought
- RSI < 30 = Oversold
- Divergence = Trend reversal
Best for: Range-bound markets
```

**2. MACD (Moving Average Convergence Divergence)**
```
Purpose: Trend direction and momentum
Components: MACD line, Signal line, Histogram
Signals:
- MACD crosses above signal = Buy
- MACD crosses below signal = Sell
- Histogram growing = Strong trend
Best for: Trending markets
```

**3. Bollinger Bands**
```
Purpose: Volatility and price extremes
Components: Upper, Middle (SMA), Lower bands
Signals:
- Price at upper band = Overbought
- Price at lower band = Oversold
- Band squeeze = Low volatility (breakout coming)
- Band expansion = High volatility
Best for: Breakout strategies
```

**4. ATR (Average True Range)**
```
Purpose: Volatility measurement
Use cases:
- Stop loss placement (SL = Entry ± 2×ATR)
- Position sizing
- Volatility filters
Note: Does NOT indicate direction!
```

**5. Stochastic Oscillator**
```
Purpose: Overbought/oversold + momentum
Range: 0-100
Signals:
- %K > 80 = Overbought
- %K < 20 = Oversold
- %K crosses %D = Entry signal
Best for: Range-bound markets
```

---

## 6. Multi-Timeframe Indicators {#multi-timeframe}

### 🎯 MTF Indicator (Pine Script)

```pinescript
//@version=5
indicator("Multi-Timeframe RSI", overlay=false)

// Current timeframe RSI
rsi1 = ta.rsi(close, 14)
plot(rsi1, "Current TF RSI", color=color.blue, linewidth=2)

// Higher timeframe RSIs
rsi_h1 = request.security(syminfo.tickerid, "60", ta.rsi(close, 14))
rsi_h4 = request.security(syminfo.tickerid, "240", ta.rsi(close, 14))
rsi_d1 = request.security(syminfo.tickerid, "D", ta.rsi(close, 14))

plot(rsi_h1, "H1 RSI", color=color.orange)
plot(rsi_h4, "H4 RSI", color=color.red)
plot(rsi_d1, "D1 RSI", color=color.purple, linewidth=2)

// Levels
hline(70, "Overbought", color=color.red)
hline(30, "Oversold", color=color.green)
```

---

## 7. Alert Systems & Webhooks {#alerts-webhooks}

### 🎯 Alert System (MQL4)

```mql4
void SendAlertNotification(string message)
{
   // Terminal alert
   Alert(message);

   // Mobile push notification
   SendNotification(message);

   // Email alert
   SendMail("Trading Alert", message);

   // Write to file log
   int fileHandle = FileOpen("alerts.log", FILE_READ|FILE_WRITE|FILE_TXT);
   if(fileHandle != INVALID_HANDLE)
   {
      FileSeek(fileHandle, 0, SEEK_END);
      FileWrite(fileHandle, TimeToString(TimeCurrent()) + ": " + message);
      FileClose(fileHandle);
   }
}
```

### 🎯 Webhook Integration (Pine Script)

```pinescript
//@version=5
indicator("Webhook Alerts", overlay=true)

rsi = ta.rsi(close, 14)

// Alert conditions
oversold = ta.crossover(rsi, 30)
overbought = ta.crossunder(rsi, 70)

// JSON message for webhook
buyMessage = '{"action":"BUY","symbol":"' + syminfo.ticker + '","price":' + str.tostring(close) + '}'
sellMessage = '{"action":"SELL","symbol":"' + syminfo.ticker + '","price":' + str.tostring(close) + '}'

if oversold
    alert(buyMessage, alert.freq_once_per_bar)
if overbought
    alert(sellMessage, alert.freq_once_per_bar)
```

---

## 8. Repainting Prevention {#repainting-prevention}

### 🎯 Common Repainting Causes

**1. Using Current Bar Data**
```pinescript
// ❌ REPAINTS (uses real-time bar)
rsi = ta.rsi(close, 14)

// ✅ NO REPAINT (uses confirmed bar)
rsi = ta.rsi(close[1], 14)
```

**2. Using `security()` Without Lookahead**
```pinescript
// ❌ REPAINTS
htf_close = request.security(syminfo.tickerid, "D", close)

// ✅ NO REPAINT
htf_close = request.security(syminfo.tickerid, "D", close, lookahead=barmerge.lookahead_on)
```

**3. Using `barstate.islast` Incorrectly**
```pinescript
// ✅ Calculate only on confirmed bars
if barstate.isconfirmed
    // Your logic here
```

### 🎯 Repainting Test Checklist

```
✅ Replay chart in TradingView
✅ Check signals don't disappear
✅ Compare live vs historical signals
✅ Test on different timeframes
✅ Verify with Strategy Tester
```

---

## 9. Performance Optimization {#performance-optimization}

### 🎯 Optimization Tips

**1. Reduce Calculations**
```python
# ❌ Slow (recalculates every time)
for i in range(len(df)):
    df.loc[i, 'ma'] = df['close'].iloc[i-20:i].mean()

# ✅ Fast (vectorized)
df['ma'] = df['close'].rolling(window=20).mean()
```

**2. Use Built-in Functions**
```mql4
// ✅ Use built-in iMA() instead of manual calculation
double ma = iMA(NULL, 0, 20, 0, MODE_SMA, PRICE_CLOSE, 0);
```

**3. Limit Historical Calculations**
```mql4
// Only recalculate new bars
int start = prev_calculated - 1;
if(start < period) start = period;

for(int i = start; i < rates_total; i++)
{
    // Calculate only new bars
}
```

---

## 10. Visualization & UI {#visualization}

### 🎯 Custom Colors & Styles

**Pine Script:**
```pinescript
//@version=5
indicator("Custom Visuals", overlay=true)

// Dynamic color based on condition
rsi = ta.rsi(close, 14)
dynamicColor = rsi > 70 ? color.red : rsi < 30 ? color.green : color.gray

plot(close, "Price", color=dynamicColor, linewidth=3)

// Gradient fill
ma20 = ta.sma(close, 20)
ma50 = ta.sma(close, 50)

plot(ma20, "MA 20", color=color.blue)
plot(ma50, "MA 50", color=color.red)
fill(plot(ma20), plot(ma50), color=color.new(color.blue, 90))
```

---

## 📚 Indicator Development Checklist

**Before Publishing:**
```
✅ Test on multiple timeframes
✅ Test on multiple symbols
✅ Check for repainting
✅ Optimize performance
✅ Add clear documentation
✅ Include usage examples
✅ Set proper default values
✅ Add alert conditions
✅ Test with real-time data
✅ Get feedback from users
```

---

## 🎯 Key Takeaways

**✅ Best Practices:**
- Keep indicators simple
- Avoid repainting
- Optimize for performance
- Use vectorized operations (Python)
- Test thoroughly before using live
- Combine multiple indicators for confirmation
- Understand what you're measuring

**❌ Common Mistakes:**
- Using too many indicators (analysis paralysis)
- Repainting indicators in production
- Optimizing on past data only (curve fitting)
- Ignoring computational cost
- Not understanding indicator limitations

---

**Master these indicators and you'll have the foundation for any trading strategy!** 🚀
